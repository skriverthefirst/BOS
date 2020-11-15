import 'package:flutter/material.dart';
import 'package:som/pages/globals/texts.dart';
import 'package:http/http.dart' as http;
import '../globals/menuClass.dart';
import '../globals/globals.dart';
import 'dart:convert';
import 'TableNumberPage.dart';

class ReceiptPage extends StatelessWidget {
  final List<Menu> chosenMenuList;

  ReceiptPage(this.chosenMenuList);

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
        body: Column(
          children: <Widget>[
            Container(
              height: (MediaQuery.of(context).size.height) / 3 * 2,
              child: Column(
                children: chosenMenuList.map<Widget>((menu)=>Container(
                    child: Column(
                      children: [
                        Text(menu.title)
                      ]
                    ),
                  ),
                ).toList(),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                IconButton(
                  icon: Icon(Icons.check),
                  onPressed: () {
                    FutureBuilder(
                      future: http.post(putOrderUrl, body: createJsonString(chosenMenuList)),
                      builder: (context, snapshot) {
                      },
                    );
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => TableNumberPage())
                    );
                  },
                ),
                IconButton(
                  icon: Icon(Icons.cancel),
                  onPressed: () => Navigator.of(context).pop(),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

String createJsonString(final List<Menu> chosenMenuList) {
  var jsonString = [{"Food":[]}];

  for(var menu in chosenMenuList) {
    jsonString[0]['Food'].add(menu);
  }

  return json.encode(jsonString);

}