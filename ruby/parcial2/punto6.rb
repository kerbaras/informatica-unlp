require 'sinatra'

get '/users/:id' do
  "Usuario #{params[:id]}"
end

post '/users/:id' do
  halt 404
end
