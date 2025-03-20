package com.docker.example1;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        // Create the server on port 8080
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/greet", new GreetHandler());
        server.setExecutor(null); // Default executor
        server.start();
        System.out.println("Server started on port 8080");
    }

    static class GreetHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {

            String query = exchange.getRequestURI().getQuery();
            String response = "Please provide input using ?input=<your_name>";

            if (query != null && query.contains("input=")) {
                // Extract input parameter
                Map<String, String> queryParams = parseQueryParams(query);
                String input = queryParams.get("input");

                response = "{\"message\": \"Hello, " + input + "!\"}";
            }

            // Send response
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.getBytes().length);

            try (OutputStream os = exchange.getResponseBody()) {
                os.write(response.getBytes());
            }
        }

        // Helper method to parse query parameters into a map
        private Map<String, String> parseQueryParams(String query) {
            Map<String, String> queryParams = new java.util.HashMap<>();
            String[] pairs = query.split("&");
            for (String pair : pairs) {
                String[] keyValue = pair.split("=");
                if (keyValue.length > 1) {
                    queryParams.put(keyValue[0], keyValue[1]);
                }
            }
            return queryParams;
        }
    }
}
