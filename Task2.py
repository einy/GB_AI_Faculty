def dataout(name, secondname, year, city, email, phone):
    return f"Имя: {name}, Фамилия: {secondname}, Год рождения: {year}, Город проживания: {city}, email: {email}, Телефон: {phone}"


print(dataout(name="John", secondname="Doe", year="666 AD", city = "Inferno", email = "me@hell.com", phone = "+666 666 666"))
