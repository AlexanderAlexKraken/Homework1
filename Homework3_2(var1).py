print("Снова здраствуйте! Сегодня захотелось познакомится поближе. Помогите мне написать программу, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон")

personal_data = [input("Ваше имя?: ")]
personal_data.append(input("Ваша фамилия?:"))
personal_data.append(input("Ваш год рождения?: "))
personal_data.append(input("Ваш город проживания?: "))
personal_data.append(input("Ваш email?: "))
personal_data.append(input("Ваш телефон?: "))
print(personal_data)
print(" Спасибо за участие в опросе!")