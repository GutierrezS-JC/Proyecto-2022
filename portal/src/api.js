import axios from "axios";

const apiService = axios.create({
    baseURL: 'http://localhost:5000/',
    withCredentials: true,
    xsrfCookieName: 'csrf_access_token'
});

export { apiService }