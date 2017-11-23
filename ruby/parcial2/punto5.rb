require 'sinatra'

get '/users/:id' do
  "Usuario común #{params[:id]}"
end

get '/users/1' do
  "Usuario especial!"
end

