require 'sinatra'

$inventory = [
    {
        'id' => 1,
        'name' => 'Item 1',
        'stock' => 20.0,
        'price' => 10.0
    },
    {
        'id' => 2,
        'name' => 'Item 2',
        'stock' => 2.0,
        'price' => 5.0
    }
]


get '/items' do
    $inventory.map { |item| item['name'] }.join(', ')
end

get '/total/:ids' do
    ids = params['ids'].split(',').map{ |n| n.to_i }
    $inventory.select { |item| ids.include? item['id']}.inject(0) { |sum, item| sum + (item['price'] * item['stock']) }.to_s
end

post '/items' do
    
    item = {
        'id' => $inventory.length + 1,
        'name' => params['name'],
        'price' => params['price'],
        'stock' => params['stock']
    }

    if item.values.find_index(nil)
        halt 422, 'The item cannot be added'
    end

    item['price'] = item['price'].to_f
    item['stock'] = item['stock'].to_f

    $inventory.push(item)
    [ 201, 'item added']

end