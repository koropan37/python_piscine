def main():
    ft_list = ["Hello"]  # 中身を変更可能
    ft_tuple = ("Hello", "toto!")  # 中身の変更は不可能
    ft_set = {"Hello", "Hello", "tutu!"}  # 重複は削除される
    ft_dict = {"Hello": "titi!"}  # 再代入

    ft_list.append("World")
    ft_tuple = (ft_tuple[0], "Japan!")
    ft_set -= {"tutu!"}  # ft_set.remove("tutu!")
    ft_set |= {"Tokyo!"}  # ft_set.add("Tokyo!")
    ft_dict["Hello"] = "42Tokyo!"
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
