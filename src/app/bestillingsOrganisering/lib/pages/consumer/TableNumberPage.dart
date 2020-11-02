import 'package:flutter/material.dart';

import 'package:flutter/material.dart';

class TableNumberPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text("Restaurant name"),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Container(
              height: (MediaQuery.of(context).size.height) / 4,
              child: Text("Welcome to the restaurant, please insert your table number below!"),
            ),
            Container(
              height: (MediaQuery.of(context).size.height) / 4,
              width: (MediaQuery.of(context).size.width) / 4,
              child: TextField(
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: "Tabel Number",
                ),
              ),
            ),
            Container(
              height: (MediaQuery.of(context).size.height) / 4
            ),
          ],
        ),
      ),
    );
  }
}