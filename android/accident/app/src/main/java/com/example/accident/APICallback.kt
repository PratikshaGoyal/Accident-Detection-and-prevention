package com.example.accident

interface APICallback {
    fun success(response : Any)
    fun failure(errorString : String)
}