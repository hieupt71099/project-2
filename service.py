from mongoengine import *
from models.user import User
from models.product import Product

def create_user(email, password, firstname, lastname, phone):
    all_user = User.objects(email=email)

    if len(all_user) > 0:
        return False
    else:
        try:
            new_user = User(
                email = email,
                password = password,
                firstname = firstname,
                lastname = lastname,
                phone = phone
            ) 
            new_user.save()
            return True
        except:
            return False

def validate_user(email, password):
    found_user = User.objects(email=email,password=password)
    if found_user:
        found_user = User.objects.get(email=email,password=password)
        return found_user
    else:
        return False

def get_display_product():
    found_products = Product.objects()
    products = {
        "yogurt_hot_deal": [],
        "yogurt": [],
        "snack": []
    }
    for p in found_products:
        p_dict = p.to_dict()
        if "hot deal" in p_dict['tag']:
            products['yogurt_hot_deal'].append(p_dict)
        elif p_dict['category'] == "yogurt":
            products['yogurt'].append(p_dict)
        elif p_dict['category'] == "snack":
            products['snack'].append(p_dict)
    return products


if __name__ == "__main__":
    import db
    db.connect()
    product = [
        {
            "image": "trân châu đường đen.jpeg",
            "name": "Sữa chua trân châu đường đen",
            "category": "yogurt",
            "tag": ["hot deal"],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Cùng với cốc trân châu đường đen Hàn Quốc thơm ngon và vô cùng hấp dẫn. Sự lựa chọn hoàn hảo cho khách hàng mọi lứa tuổi.",
            "price": 30000,
        },
        {
            "image": "tươi trân châu đường đen.jpeg",
            "name": "Sữa tươi trân châu đường đen",
            "category": "yogurt",
            "tag": ["hot deal"],
            "description": "Sữa tươi nguyên kem béo ngậy cùng với trân châu đường đen Hàn Quốc thơm ngon và vô cùng mới là sự lựa chọn hoàn hảo cho khách hàng mọi lứa tuổi.",
            "price": 35000,
        },
        {
            "image": "trân châu Quảng Ninh.jpeg",
            "name": "Sữa chua trân châu Quảng Ninh",
            "category": "yogurt",
            "tag": ["hot deal"],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Cùng với cốc trân châu dai, mềm, ủ trong cốt dừa thơm ngậy. Sự lựa chọn hoàn hảo cho khách hàng mọi lứa tuổi.",
            "price": 25000,
        },
        {
            "image": "đào.jpg",
            "name": "Sữa chua đào",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp siro đào và topping đào ngâm. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "đậu đỏ.jpg",
            "name": "Sữa chua đậu đỏ",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long.Thêm vào đó là topping đậu đỏ thơm ngon. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        # ...
        {
            "image": "thập cẩm.jpg",
            "name": "Sữa chua thập cẩm",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Kèm theo là topping đầy ú ụ, bao gồm: dứa hấu, mít, xoài. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 30000,
        },
        {
            "image": "dâu tây.jpg",
            "name": "Sữa chua dâu tây",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp siro dâu tây kèm theo vài lát dâu tây tươi ngon. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 30000,
        },
        {
            "image": "chanh leo.jpg",
            "name": "Sữa chua chanh leo",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp siro chanh leo. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "xoài.jpg",
            "name": "Sữa chua xoài",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Kèm theo là topping xoài thái hạt lựu. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "socola.jpg",
            "name": "Sữa chua socola",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp socola ngọt ngào. Phù hợp với khách hàng thích đồ ngọt. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "nếp cẩm.jpg",
            "name": "Sữa chua nếp cẩm",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Kèm theo là topping nếp cẩm dẻo ngon. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "matcha.jpg",
            "name": "Sữa chua matcha",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp matcha trà xanh. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "cà phê.jpg",
            "name": "Sữa chua cà phê",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp cafe thơm ngon. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "kiwi.jpg",
            "name": "Sữa chua kiwi",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Rưới lên trên là 1 lớp kiwi. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 30000,
        },
        {
            "image": "sen vàng.jpg",
            "name": "Sữa chua sen vàng",
            "category": "yogurt",
            "tag": [],
            "description": "Sữa chua dạng kem, mát dẻo, lại tốt cho sức khỏe, chuẩn vị Hạ Long. Thêm vào đỏ là những hạt sen vàng thơm ngon. Lưu ý: sản phẩm chưa bao gồm trân châu cốt dừa.",
            "price": 25000,
        },
        {
            "image": "bo-kho.jpeg",
            "name": "Bò khô",
            "category": "snack",
            "tag": [],
            "description": "",
            "price": 25000,
        },
        {
            "image": "ga-kho.jpeg",
            "name": "Gà khô",
            "category": "snack",
            "tag": [],
            "description": "",
            "price": 25000,
        },
        {
            "image": "huong-duong.jpeg",
            "name": "Hướng dương",
            "category": "snack",
            "tag": [],
            "description": "",
            "price": 10000,
        },
    ]
    # for i in range(len(product)):
    #     print(i)
    #     new_product = Product(**product[i])
    #     new_product.save()

    print(get_display_product())
    