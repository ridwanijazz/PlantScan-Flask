package com.example.plantsscanning.ui.analisis

import android.content.Intent
import android.graphics.BitmapFactory
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.plantsscanning.R
import com.example.plantsscanning.databinding.ActivityDetailAnalisisBinding
import com.example.plantsscanning.databinding.ActivityUploadBinding
import com.example.plantsscanning.ui.MainActivity

class DetailAnalisisActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDetailAnalisisBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDetailAnalisisBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //val imageBase64 = intent.getStringExtra("IMAGE_BASE64")

        val diseaseName = intent.getStringExtra("DISEASE_NAME") ?: "Unknown Disease"
        val description = intent.getStringExtra("DESCRIPTION") ?: "No Description"
        val action = intent.getStringExtra("ACTION") ?: "No Action"
        val image = intent.getByteArrayExtra("IMAGE")

        binding.tvDiseaseName.text = diseaseName
        binding.tvDiseaseDetail.text=description
        binding.tvSolutionDetail.text=action


        image.let {
            val bitmap = BitmapFactory.decodeByteArray(image, 0, image?.size ?: 0)
            binding.plantImage.setImageBitmap(bitmap)
        }


        binding.btnBack.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            intent.flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
            startActivity(intent)
            finish()
        }

    }


}