import speedtest


def test_internet_speed():
    st = speedtest.Speedtest()

    # Получаем лучший сервер на основе пинга
    st.get_best_server()

    # Измеряем скорость загрузки (в битах в секунду) и конвертируем в Мбит/c
    download_speed = st.download() / 1_000_000

    # Измеряем скорость отдачи (в битах в секунду) и конвертируем в Мбит/c
    upload_speed = st.upload() / 1_000_000

    # Измеряем пинг
    ping_result = st.results.ping

    # Получаем IP-адрес, провайдера и город
    client_info = st.results.client
    ip_address = client_info.get('ip', 'Недоступно')
    isp = client_info.get('isp', 'Недоступно')
    city = client_info.get('city', 'Недоступно')

    return download_speed, upload_speed, ping_result, ip_address, isp, city


# Попробуйте вызвать функцию и вывести результаты
try:
    download, upload, ping, ip, provider, city = test_internet_speed()
    print(f"Скорость загрузки: {download:.2f} Мбит/с")
    print(f"Скорость отдачи: {upload:.2f} Мбит/с")
    print(f"Пинг: {ping:.2f} мс")
    print(f"IP-адрес: {ip}")
    print(f"Провайдер: {provider}")
    print(f"Город: {city}")
except Exception as e:
    print(f"Произошла ошибка при измерении скорости интернета: {e}")
