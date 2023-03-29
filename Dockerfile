# Stage 1: Build the React app
FROM node:14.17.6-alpine
#AS build

ARG GITHUB_RUN_NUMBER=123

ENV GITHUB_RUN_NUMBER=${GITHUB_RUN_NUMBER}

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app code
COPY . .

# Build the app for production
RUN npm run build
EXPOSE 3000

CMD [ "npm" , "start"]

# Stage 2: Serve the app with Nginx
#FROM nginx:1.21.3-alpine

# Copy the Nginx configuration file
#COPY nginx.conf /etc/nginx/nginx.conf

# Copy the built React app from the previous stage
#COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for the Nginx server
#EXPOSE 80

# Start Nginx when the container starts
#CMD ["nginx", "-g", "daemon off;"]

