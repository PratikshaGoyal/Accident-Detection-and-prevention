package com.example.accident

import android.support.design.widget.TextInputEditText
import com.example.accident.activities.LoginActivity
import com.example.accident.helpers.DatabaseHelper
import com.example.accident.model.StatusResponse
import com.google.gson.annotations.JsonAdapter
import okhttp3.RequestBody
import retrofit2.Call
import retrofit2.http.*

interface APIInterface {
//    @Header("Content-Type:application/json")
//    @FormUrlEncoded
    @POST("users/")
    fun createUser(@Body request: RequestBody):Call<StatusResponse>
//        @Field("name") name: String,
//        @Field("num") num: String,
//        @Field("enum") enum: String,
//        @Field("email") email: String,
//        @Field("password") password: String
//    ):Call<StatusResponse>

    @POST("location/")
    fun location(@Body request: RequestBody):Call<StatusResponse>



}