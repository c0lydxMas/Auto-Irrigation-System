package com.example.embeddedsystem;

import java.util.Date;

public class SoilMoisture {
//    private Date date;
    private int soil_moisture;

    public SoilMoisture(int soil_moisture) {
//        this.date = date;
        this.soil_moisture = soil_moisture;
    }

//    public Date getDate() {
//        return date;
//    }
//
//    public void setDate(Date date) {
//        this.date = date;
//    }

    public int getSoil_moisture() {
        return soil_moisture;
    }

    public void setSoil_moisture(int soil_moisture) {
        this.soil_moisture = soil_moisture;
    }
}
