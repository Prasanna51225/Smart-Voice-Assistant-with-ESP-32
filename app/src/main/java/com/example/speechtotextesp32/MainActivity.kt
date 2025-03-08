package com.example.SpeechToTextESP32  // Replace with your actual package name
import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.speech.RecognitionListener
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.widget.Button
import android.widget.LinearLayout
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import java.net.Socket
import kotlin.concurrent.thread


class MainActivity : AppCompatActivity() {
    private lateinit var speechRecognizer: SpeechRecognizer

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Use Kotlin DSL to create a button programmatically
        setContentView(
            LinearLayout(this).apply {
                orientation = LinearLayout.VERTICAL

                addView(Button(this@MainActivity).apply {
                    text = "Speak"
                    setOnClickListener { startSpeechRecognition() }
                })
            }
        )

        // Initialize SpeechRecognizer
        speechRecognizer = SpeechRecognizer.createSpeechRecognizer(this)
    }

    // Function to start speech recognition
    private fun startSpeechRecognition() {
        // Create an intent for speech recognition
        val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
            putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
            putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US")
        }

        // Set recognition listener for handling speech recognition results
        speechRecognizer.setRecognitionListener(object : RecognitionListener {
            override fun onResults(results: Bundle?) {
                val matches = results?.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)
                matches?.let {
                    val recognizedText = it[0].lowercase()
                    sendDataToESP32(recognizedText) // Send recognized text to ESP32
                }
            }

            // Required override methods for RecognitionListener
            override fun onReadyForSpeech(params: Bundle?) {}
            override fun onError(error: Int) {}
            override fun onBeginningOfSpeech() {}
            override fun onBufferReceived(buffer: ByteArray?) {}
            override fun onEndOfSpeech() {}
            override fun onEvent(eventType: Int, params: Bundle?) {}
            override fun onPartialResults(partialResults: Bundle?) {}
            override fun onRmsChanged(rmsdB: Float) {}
        })

        // Start listening for speech input
        speechRecognizer.startListening(intent)
    }

    // Function to send data (recognized text) to ESP32 via socket
    private fun sendDataToESP32(text: String) {
        thread {
            try {
                val socket = Socket("192.168.48.178", 80)  // Use ESP32 IP
                val writer = socket.getOutputStream().writer()
                writer.write(text + "\n")
                writer.flush()
                writer.close()
                socket.close()
            } catch (e: Exception) {
                runOnUiThread {
                    Toast.makeText(this, "Error: ${e.message}", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }
}
