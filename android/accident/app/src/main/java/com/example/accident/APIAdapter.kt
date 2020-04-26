package com.example.accident

import okhttp3.HttpUrl
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory



class APIAdapter {
    companion object {
        val baseUrl = "http://server_ip:8000/"
        val httpLoggerInterceptor = HttpLoggingInterceptor().setLevel(HttpLoggingInterceptor.Level.BODY)
        var okHttpClient = OkHttpClient.Builder().addInterceptor(httpLoggerInterceptor).build()


        var retrofit: Retrofit? = null

        fun getApiClient(apiInterface: Class<APIInterface>): APIInterface {
            if (retrofit == null) {
                retrofit = prepareRetrofit()
            }
            return retrofit!!.create(apiInterface)

        }

        private fun prepareRetrofit(): Retrofit {

            retrofit = Retrofit.Builder()
                .baseUrl(baseUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .client(okHttpClient)
                .build()

            return retrofit as Retrofit
        }
    }
}

