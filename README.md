# Aquaemi-ARIMA
# Overview
Nhận ra tầm quan trọng của việc dự đoán chất lượng nước trong tương lai, chúng em đã thu thập dữ liệu của sông Mê-kông tại Cần Thơ từ 15/01/2003-15/12/2021 từ MRC (Mekong River Commission) để tạo ra một mô hình time-series ứng dụng ARIMA (autoregressive integrated moving average) với độ chính xác lên đến 91.4%.

# Methodology
Chúng em sử dụng các công nghệ như Pandas, Jupyter Notebook, Statsmodels, sktime, matplotlib để nghiên cứu và nhận ra được tính mùa (seasonality) của các trường dữ liệu thu thập được.

Chúng em đã sử dụng ensemble learning bằng cách train từng field data trong các trường Chemical Oxygen Demand, Dissolved Oxygen, Electrical Conductivity, pH, temperature, Nitrate concentration (NO3), Nitrogen concentration (N2), Total Suspended Solids và tổng hợp lại thành một WQI index qua việc sử dụng WAWQI (weighted average water quality index). 

Với cùng phương pháp, chúng em tách ra thành 2 model, model đầu tiên theo nguyên lý statistics và được train trên toàn bộ dữ liệu, model thứ hai theo nguyên lý machine learning và data được chia ra thành train và test set.

# Results
MAPE (mean absolute percentage error) thấp hơn 8.6% (đồng nghĩa chính xác 91.4%) với mô hình train đến từ năm 2016 đến 2021, và với độ chính xác 90.5% đối với mô hình train từ 2014-2019 và test dựa vào forecast các năm 2020-2021. 

# Cách sử dụng
1. pip install -r requirements.txt
2. Sử dụng forecast.py và dùng find_best_model() để train được model tối ưu cho dữ liệu.
3. Sử dụng forecast() để dự báo predicted_mean, lower_bound, và upper_bound
