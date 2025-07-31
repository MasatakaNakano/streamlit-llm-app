person = {"name": "山田太郎", "age": 30, "prefecture": "東京都"}
person["job"] = "エンジニア"

# personの値だけを要素に持つリストを作成
person_values = list(person.values())
print(person_values)  # ['山田太郎', 30, '東京都', 'エンジニア']

for key, value in person.items():

    print(f"{key}: {value}")



# 以下はサンプルとして0から9までを表示するループです（例示・デバッグ目的）
for i in range(10):
    print(i)



def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """

    return base * height / 2

# リストから偶数だけを抽出する関数
def extract_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result