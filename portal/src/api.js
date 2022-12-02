import axios from "axios";

const apiService = axios.create({
    // baseURL: 'http://localhost:5000/',
    baseURL: 'https://admin-grupo26.proyecto2022.linti.unlp.edu.ar/',
    withCredentials: true,
    xsrfCookieName: 'csrf_access_token',
    xsrfHeaderName: "X-CSRF-TOKEN"
});

export { apiService }