# 定义类型的种类
def switch_string_poetry(argument):
    switcher = {0:"text",1:"src",2:u"stripped"}
    result = switcher.get(argument);
    if result is None:
        result = "\nDefault.";
    return result;
# html 元素遍历 目前仅向下一层 var结构
def html_attr_trav(type,datas):
        result = [];
        if datas is None or type is None:
            return "Error:传输的数据结构有误,没有匹配到key所对应的值!"
        for data in datas:
            if type == 0:
                result.append(data.get_text());
            elif type == 1:
                result.append(data.get('src'));
            elif type == 2:
                result.append(list(data.stripped_strings))
            else:
                return "Error:不匹配的数据类型!";
        return result;