package com.example.accident.activities

import android.annotation.SuppressLint
import android.os.Bundle
import android.support.design.widget.Snackbar
import android.support.design.widget.TextInputEditText
import android.support.design.widget.TextInputLayout
import android.support.v4.widget.NestedScrollView
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.AppCompatButton
import android.support.v7.widget.AppCompatTextView
import android.view.View
import android.widget.Toast
import com.example.accident.*
import com.example.accident.helpers.DatabaseHelper
import com.example.accident.model.StatusResponse
import com.example.accident.model.User
import kotlinx.android.synthetic.main.activity_register.*
import okhttp3.MediaType
import okhttp3.RequestBody
import org.json.JSONObject
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

//import com.androidtutorialshub.loginregisterkotlin.R
//import com.androidtutorialshub.loginregisterkotlin.helpers.InputValidation
//import com.androidtutorialshub.loginregisterkotlin.model.User
//import com.androidtutorialshub.loginregisterkotlin.sql.DatabaseHelper


class RegisterActivity : AppCompatActivity(), View.OnClickListener {

    private val activity = this@RegisterActivity

    private lateinit var nestedScrollView: NestedScrollView

    private lateinit var textInputLayoutName: TextInputLayout
    private lateinit var textInputLayoutNumber: TextInputLayout
    private lateinit var textInputLayoutEmergency: TextInputLayout
    private lateinit var textInputLayoutVehicle: TextInputLayout
    private lateinit var textInputLayoutEmail: TextInputLayout
    private lateinit var textInputLayoutPassword: TextInputLayout
    private lateinit var textInputLayoutConfirmPassword: TextInputLayout

    private lateinit var textInputEditTextName: TextInputEditText
    private lateinit var textInputEditTextNumber: TextInputEditText
    private lateinit var textInputEditTextEmergency: TextInputEditText
    private lateinit var textInputEditTextVehicle: TextInputEditText
    private lateinit var textInputEditTextEmail: TextInputEditText
    private lateinit var textInputEditTextPassword: TextInputEditText
    private lateinit var textInputEditTextConfirmPassword: TextInputEditText

    private lateinit var appCompatButtonRegister: AppCompatButton
    private lateinit var appCompatTextViewLoginLink: AppCompatTextView

    private lateinit var inputValidation: InputValidation
    private lateinit var databaseHelper: DatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_register)

        // hiding the action bar
        supportActionBar!!.hide()

        // initializing the views
        initViews()

        // initializing the listeners
        initListeners()

        // initializing the objects
        initObjects()
    }

    /**
     * This method is to initialize views
     */
    private fun initViews() {
        nestedScrollView = findViewById<View>(R.id.nestedScrollView) as NestedScrollView

        textInputLayoutName = findViewById<View>(R.id.textInputLayoutName) as TextInputLayout
        textInputLayoutNumber = findViewById<View>(R.id.textInputLayoutNumber) as TextInputLayout
        textInputLayoutEmergency = findViewById<View>(R.id.textInputLayoutEmergency) as TextInputLayout
        textInputLayoutVehicle = findViewById<View>(R.id.textInputLayoutVehicle) as TextInputLayout
        textInputLayoutEmail = findViewById<View>(R.id.textInputLayoutEmail) as TextInputLayout
        textInputLayoutPassword = findViewById<View>(R.id.textInputLayoutPassword) as TextInputLayout
        textInputLayoutConfirmPassword = findViewById<View>(R.id.textInputLayoutConfirmPassword) as TextInputLayout

        textInputEditTextName = findViewById<View>(R.id.textInputEditTextName) as TextInputEditText
        textInputEditTextNumber = findViewById<View>(R.id.textInputEditTextNumber) as TextInputEditText
        textInputEditTextEmergency = findViewById<View>(R.id.textInputEditTextEmergency) as TextInputEditText
        textInputEditTextVehicle = findViewById<View>(R.id.textInputEditTextVehicle) as TextInputEditText
        textInputEditTextEmail = findViewById<View>(R.id.textInputEditTextEmail) as TextInputEditText
        textInputEditTextPassword = findViewById<View>(R.id.textInputEditTextPassword) as TextInputEditText
        textInputEditTextConfirmPassword = findViewById<View>(R.id.textInputEditTextConfirmPassword) as TextInputEditText

        appCompatButtonRegister = findViewById<View>(R.id.appCompatButtonRegister) as AppCompatButton

        appCompatTextViewLoginLink = findViewById<View>(R.id.appCompatTextViewLoginLink) as AppCompatTextView

    }

    /**
     * This method is to initialize listeners
     */
    private fun initListeners() {
        appCompatButtonRegister!!.setOnClickListener(this)
        appCompatTextViewLoginLink!!.setOnClickListener(this)

    }

    /**
     * This method is to initialize objects to be used
     */
    private fun initObjects() {
        inputValidation = InputValidation(activity)
        databaseHelper = DatabaseHelper(activity)


    }


    /**
     * This implemented method is to listen the click on view
     *
     * @param v
     */
    override fun onClick(v: View) {
        when (v.id) {

            R.id.appCompatButtonRegister -> postDataToSQLite()

            R.id.appCompatTextViewLoginLink -> finish()
        }
    }

    /**
     * This method is to validate the input text fields and post data to SQLite
     */
    private fun postDataToSQLite() {
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextName, textInputLayoutName, getString(R.string.error_message_name))) {
            return
        }
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextNumber, textInputLayoutNumber, getString(R.string.error_message_number))) {
            return
        }
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextEmail, textInputLayoutEmergency, getString(R.string.error_message_emergency))) {
            return
        }
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextEmail, textInputLayoutVehicle, getString(R.string.error_message_vehicle))) {
            return
        }
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextEmail, textInputLayoutEmail, getString(R.string.error_message_email))) {
            return
        }
        if (!inputValidation!!.isInputEditTextEmail(textInputEditTextEmail, textInputLayoutEmail, getString(R.string.error_message_email))) {
            return
        }
        if (!inputValidation!!.isInputEditTextFilled(textInputEditTextPassword, textInputLayoutPassword, getString(R.string.error_message_password))) {
            return
        }
        if (!inputValidation!!.isInputEditTextMatches(textInputEditTextPassword, textInputEditTextConfirmPassword,
                textInputLayoutConfirmPassword, getString(R.string.error_password_match))) {
            return
        }

        if (!databaseHelper!!.checkUser(textInputEditTextEmail!!.text.toString().trim())) {

            var user = User(
                name = textInputEditTextName!!.text.toString().trim(),
                num = textInputEditTextNumber!!.text.toString().trim(),
                enum = textInputEditTextEmergency!!.text.toString().trim(),
                vehicle = textInputEditTextVehicle!!.text.toString().trim(),
                email = textInputEditTextEmail!!.text.toString().trim(),
                password = textInputEditTextPassword!!.text.toString().trim()
            )

            databaseHelper!!.addUser(user)

            //post to server
            val name = textInputEditTextName!!.text.toString().trim()
            val num = textInputEditTextNumber!!.text.toString().trim()
            val enum = textInputEditTextEmergency!!.text.toString().trim()
            val vehicle = textInputEditTextVehicle!!.text.toString().trim()
            val email = textInputEditTextEmail!!.text.toString().trim()
            val password = textInputEditTextPassword!!.text.toString().trim()





            val json = JSONObject()
            json.put("name", name)
            json.put("num", num)
            json.put("enum", enum)
            json.put("vehicle", vehicle)
            json.put("email", email)
            json.put("password", password)
            val requestBody: RequestBody = RequestBody.create(MediaType.parse("application/json"), json.toString())
            val call: Call<StatusResponse> = APIAdapter.getApiClient(APIInterface::class.java).createUser(requestBody)
//            val call: Call<StatusResponse> = RetrofitClient.instance.createUser(requestBody)

            call.enqueue(object: Callback<StatusResponse>{
                    override fun onFailure(call: Call<StatusResponse>, t: Throwable) {
                        Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
                    }

                    override fun onResponse(call: Call<StatusResponse>, response: Response<StatusResponse>) {
                        Toast.makeText(applicationContext, response.body()?.message, Toast.LENGTH_LONG).show()
                    }

                })

//            RetrofitClient.instance.createUser(name, num, enum, email, password)
//                .enqueue(object: Callback<StatusResponse>{
//                    override fun onFailure(call: Call<StatusResponse>, t: Throwable) {
//                        Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
//                    }
//
//                    override fun onResponse(call: Call<StatusResponse>, response: Response<StatusResponse>) {
//                        Toast.makeText(applicationContext, response.body()?.message, Toast.LENGTH_LONG).show()
//                    }
//
//                })

//            APIAdapter.getApiClient(APIInterface::class.java).createUser(name, num, enum, email, password)
//                .enqueue(object : Callback<StatusResponse> {
//                    override fun onFailure(call: Call<StatusResponse>, t: Throwable) {
//                        Toast.makeText(applicationContext, t.message, Toast.LENGTH_LONG).show()
//                    }
//
//                    override fun onResponse(call: Call<StatusResponse>, response: Response<StatusResponse>) {
//                        Toast.makeText(applicationContext, response.body()?.message, Toast.LENGTH_LONG).show()
//                    }
//
//                })


            // Snack Bar to show success message that record saved successfully
            Snackbar.make(nestedScrollView!!, getString(R.string.success_message), Snackbar.LENGTH_LONG).show()
            emptyInputEditText()

        }


        else {
            // Snack Bar to show error message that record already exists
            Snackbar.make(nestedScrollView!!, getString(R.string.error_email_exists), Snackbar.LENGTH_LONG).show()
        }


    }

    /**
     * This method is to empty all input edit text
     */
    private fun emptyInputEditText() {
        textInputEditTextName!!.text = null
        textInputEditTextNumber!!.text = null
        textInputEditTextEmergency!!.text = null
        textInputEditTextVehicle!!.text = null
        textInputEditTextEmail!!.text = null
        textInputEditTextPassword!!.text = null
        textInputEditTextConfirmPassword!!.text = null
    }}
