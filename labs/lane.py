# const переменные
col_columns = 4
number_surname = 0
number_name = 1
number_laba = 2
number_want = 3

#объявление базы для расчётов
list = []
col_student = 30
was_the_last_person_to_respond = 5

# вввод и сохранение всех студентов

for i in range(0, col_student):
    list.append([])
    tmp = input('Enter info about group: ')
    list[i].append(tmp.split()[0])
    list[i].append(tmp.split()[1])
    list[i].append(int(tmp.split()[2]))
    list[i].append(int(tmp.split()[3]))
print("Success! all saved")

# выщитывание среднего количества лаб
average_number_of_labs = 0
for i in range(0, col_student):
    average_number_of_labs += list[i][number_laba]
average_number_of_labs /= col_student
print("Average number of labs: ", average_number_of_labs)

# алгоритм для конечного вывода
mas_rez = []
for i in range(0, col_student):
    if list[i][number_laba] < average_number_of_labs-2 and list[i][number_want] == 1:
        mas_rez.append(list[i])

for i in range(0, col_student):
    number_for_check = (i+was_the_last_person_to_respond)%(col_student-1)
    if (list[number_for_check][number_laba] >= average_number_of_labs-2
            and list[i][number_want] == 1):
        mas_rez.append(list[number_for_check])

for i in range(0, len(mas_rez)):
    print(f"{i}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")

    #
    # # регистрация после команды start
    # class Registration(StatesGroup):
    #     user_first_name = State()
    #     user_last_name = State()
    #     extended_information = State()
    #
    #
    # @router.message(CommandStart())
    # async def cmd_start(message: Message, state: FSMContext):
    #     # await message.answer("Чтобы создать очередь, отправь сообщение в таком формате:",
    #     #                      reply_markup=types.ReplyKeyboardRemove()) #переписать
    #     # await message.answer("Иосько Михаил	3	0")
    #     # await message.answer("Нужно отправить весь список целиком и предерживаться шаблона: превые 2 слова должны содержать фамилию и имя, потом идёт номер текущей лабы и булевая переменная, которая отражает желание студента сдавать лабу на занятии")
    #     await message.answer("Введите количество студентов в группе")
    #     await rq.set_user(message.from_user.id)
    #     await state.set_state(Registration.user_first_name)
    #
    #
    # @router.message(Registration.user_first_name)
    # async def process_first_name(message: Message, state: FSMContext):
    #     await state.update_data(user_first_name=message.text)
    #     await state.set_state(Registration.user_last_name)  # Сместить в другую функцию
    #     await message.answer('Введите номер последнего, кто защищал лабу')  # переписать
    #
    #
    # @router.message(Registration.user_last_name)
    # async def process_last_name(message: Message, state: FSMContext):
    #     await state.update_data(user_last_name=message.text)
    #     await state.set_state(Registration.extended_information)
    #     await message.answer('Скидывай таблицу')
    #
    #
    # @router.message(Registration.extended_information)
    # async def extended_information(message: Message, state: FSMContext):
    #     await state.update_data(extended_information=message.text)
    #
    #     data = await state.get_data()
    #
    #     # const переменные
    #     col_columns = 4
    #     number_surname = 0
    #     number_name = 1
    #     number_laba = 2
    #     number_want = 3
    #
    #     # объявление базы для расчётов
    #     list = []
    #     col_student = int(data['user_first_name'])
    #     was_the_last_person_to_respond = int(data['user_last_name'])
    #
    #     # вввод и сохранение всех студентов
    #
    #     for i in range(0, col_student):
    #         list.append([])
    #         tmp = str(data['extended_information']).split()
    #         list[i].append(tmp[i * col_columns + number_surname])
    #         list[i].append(tmp[i * col_columns + number_name])
    #         list[i].append(int(tmp[i * col_columns + number_laba]))
    #         list[i].append(int(tmp[i * col_columns + number_want]))
    #     print("Success! all saved")
    #
    #     # выщитывание среднего количества лаб
    #     average_number_of_labs = 0
    #     for i in range(0, col_student):
    #         average_number_of_labs += list[i][number_laba]
    #     average_number_of_labs /= col_student
    #     print("Average number of labs: ", average_number_of_labs)
    #
    #     # алгоритм для конечного вывода
    #     mas_rez = []
    #     for i in range(0, col_student):
    #         if list[i][number_laba] < average_number_of_labs - 2 and list[i][number_want] == 1:
    #             mas_rez.append(list[i])
    #
    #     for i in range(0, col_student):
    #         number_for_check = (i + was_the_last_person_to_respond) % (col_student - 1)
    #         if (list[number_for_check][number_laba] >= average_number_of_labs - 2
    #                 and list[i][number_want] == 1):
    #             mas_rez.append(list[number_for_check])
    #
    #     for i in range(0, len(mas_rez)):
    #         print(f"{i}. {mas_rez[i][number_surname]} {mas_rez[i][number_name]} {mas_rez[i][number_laba]}")
    #     await message.answer()
    #     await state.clear()
    #     await message.answer('Если захочешь создать новую очередь, пиши "/start"😉')
    #     # await rq.update_money()
    # # Конец регистрации пользователя