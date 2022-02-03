package com.example.embeddedsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.github.anastr.speedviewlib.TubeSpeedometer;

import java.util.Timer;
import java.util.TimerTask;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private TextView noti;
    private Button btnCallApi;
    private TubeSpeedometer tubeSpeedometer;
    private Timer myTimer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnCallApi = findViewById(R.id.btn_call_api);
        noti = findViewById(R.id.noti);

        tubeSpeedometer = findViewById(R.id.tubeSpeedometer);
        tubeSpeedometer.setMaxSpeed(1024);
        tubeSpeedometer.setUnit("");

        myTimer = new Timer();
        myTimer.schedule(new TimerTask() {
            @Override
            public void run() {
                callApi();
            }

        }, 0, 2000);

        btnCallApi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                callApi();
            }
        });

    }

    private void callApi(){
        APIService.apiService.getData().enqueue(new Callback<SoilMoisture>() {
            @Override
            public void onResponse(Call<SoilMoisture> call, Response<SoilMoisture> response) {
                noti.setText("");
                SoilMoisture soilMoisture = response.body();
                if(soilMoisture != null){
                    tubeSpeedometer.speedTo(soilMoisture.getSoil_moisture());
                }
            }

            @SuppressLint("SetTextI18n")
            @Override
            public void onFailure(Call<SoilMoisture> call, Throwable t) {
                noti.setText("Unexpected Error!");
            }
        });
    }
}