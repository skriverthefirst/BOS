import 'package:flutter/material.dart';
import 'dart:convert';
import '../globals/texts.dart';
import 'package:flutter/services.dart' show rootBundle;


class MenuPage extends StatelessWidget {
  Future<String> loadJson() async => await rootBundle.loadString('assets/menu.txt');

  List<Menu> chosenMenuItems = [];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text(restaurant_name),
          leading: new IconButton(
            icon: new Icon(Icons.arrow_back_ios, color: Colors.white),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ),
        body: Row(
          children: <Widget>[
            Container(
              height: (MediaQuery.of(context).size.height),
              width: (MediaQuery.of(context).size.width) / 3 * 2,
              child: Container(
                child: FutureBuilder(
                  future: loadJson(),
                  builder: (context, snapshot) {
                    if(snapshot.hasData) {
                      var menus = Menu.convertSnapshotToMenus(snapshot.data);
                      return Column(
                        children: menus.map<Widget>((menu)=>Container(
                          width: (MediaQuery.of(context).size.width) / 3 * 2,
                          decoration: BoxDecoration(
                            border: Border.all(color: Colors.blueAccent)
                          ),
                          child: Row(
                            children: <Widget>[
                              Expanded(
                                flex: 15,
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: <Widget>[
                                    Text(menu.title, style: TextStyle(fontWeight: FontWeight.bold)),
                                    Container(height: 5.0),
                                    Text(menu.description),
                                    Container(height: 15.0),
                                    ],
                                  ),
                                ),
                                Expanded(
                                  flex: 2,
                                  child: Container(
                                    color: Colors.green,
                                    child: IconButton(
                                      icon: Icon(Icons.add),
                                      onPressed: () {
                                        print(menu.title);
                                      },
                                    )
                                  )
                                ),
                              ]
                            )
                          )
                        ).toList()
                      );
                    } else {
                      return Column();
                    }
                  }
                ),
              ),
            ),
            Container(
              decoration: BoxDecoration(
                border: Border.all(color: Colors.blueAccent)
              ),
              height: (MediaQuery.of(context).size.height),
              width: (MediaQuery.of(context).size.width) / 3,
              child: Column(
                children: <Widget>[
                  Expanded(
                    flex: 10,
                    child: Container(
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.blueAccent)
                      ),
                      child: Column(
                        
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 2,
                    child: SizedBox(
                      width: double.maxFinite,
                      child: TextButton(
                          child: Text("Afslut Order",
                          style: TextStyle(fontWeight: FontWeight.bold),
                        ),
                        onPressed: () {},
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

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