import 'dart:convert';

class Menu {
  final String title;
  final String description;

  Menu({this.title, this.description});

  static List<Menu> convertSnapshotToMenus(snapshotData) {
    List<Menu> listOfMenusObject = [];
    var listOfMenusJson = jsonDecode(snapshotData)['menus'];

    for(var menu in listOfMenusJson){
      Menu menuItem = Menu.fromJson(menu);
      listOfMenusObject.add(menuItem);
    }

    return listOfMenusObject;
  }

  factory Menu.fromJson(Map<String, dynamic> json) => Menu(
    title: json['title'],
    description: json['description']
  );
  Map<String, dynamic> toJson() => {
    "title": title,
    "description": description,
  };
}