from reader_stuff import reader
from writer_stuff import writer
from generator_stuff import generator


# Генерируем json-файл
generator.create_json('input', 10000)

# Считываем в словарь
reader_instance = reader
json_dict = reader_instance.read_json_data('input')

# Словарь преобразуем в строку вида json
writer_instance = writer
output_json = writer_instance.create_json_from(json_dict)

# Создаем новый файл, добавляем в него строку-json и закрываем
output_file = open('output.json', 'w')
output_file.write(output_json)
output_file.close()
