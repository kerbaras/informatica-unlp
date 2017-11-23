module Rack
    
    class Healthcheck
    
        def initialize(app, options={})
          @app  = app
        end
    
        def call(env)
            if env['PATH_INFO'] == '/healthcheck'
                return ['200', {'Content-Type' => 'text/html'}, ['App is available.']]
            else
                status, headers, body = @app.call(env)
                return [status, headers, body]
            end
        end
    end
end
    