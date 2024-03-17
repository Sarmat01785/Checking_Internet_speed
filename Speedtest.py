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

    return download_speed, upload_speed, ping_result


download, upload, ping = test_internet_speed()
print(f"Скорость загрузки: {download:.2f} Мбит/с")
print(f"Скорость отдачи: {upload:.2f} Мбит/с")
print(f"Пинг: {ping:.2f} мс")
