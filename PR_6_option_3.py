text = ("Пётр I Великий Перипетии судьбы Петра I (1672–1725), "
        "последнего русского царя и первого императора Всероссийского, вот уже "
        "три столетия занимают исследователей, политиков и литераторов. Великий реформатор перекроил российское "
        "общество, разделив историю страны на «петровскую» и «допетровскую» эпохи, а некоторые его "
        "нововведения живы и по сей день. Все действия Петра I во внутренней и внешней политике так или "
        "иначе сводились к одному: император стремился увеличить военную и техническую мощь страны, "
        "прорубить «окно в Европу» и заимствовать лучшие достижения европейской цивилизации.")
dlina = len(text)
cnt = text.count(".")
text = text.replace(".", "")
print("Было всего символов, включая пробелы,", dlina, "удалено", cnt, "точек и стало", dlina - cnt, "символов, также включая пробелы")
