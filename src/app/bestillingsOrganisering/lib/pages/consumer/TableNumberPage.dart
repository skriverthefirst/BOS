import 'package:flutter/material.dart';
import '../globals/texts.dart';
import 'MenuPage.dart';

class TableNumberPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        resizeToAvoidBottomInset: false,
        appBar: AppBar(
          title: Text(restaurant_name),
          leading: new IconButton(
            icon: new Icon(Icons.arrow_back_ios, color: Colors.white),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Container(
              height: (MediaQuery.of(context).size.height) / 4,
              width: (MediaQuery.of(context).size.width),
              alignment: Alignment.center,
              child: FittedBox(
                fit: BoxFit.fitWidth,
                child: Text(
                  welcome_text,
                  style: TextStyle(fontSize: 25.0),
                ),
              ),
            ),
            Container(
              height: (MediaQuery.of(context).size.height) / 4,
              width: (MediaQuery.of(context).size.width) / 3,
              alignment: Alignment.center,
              child: TextField(
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: table_number,
                ),
              ),
            ),
            Container(
              height: (MediaQuery.of(context).size.height) / 4,
              alignment: Alignment.center,
              child: FloatingActionButton(
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(16.0))),
                child: Icon(Icons.check),
                onPressed: (){
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => MenuPage())
                  );
                },
              )
            ),
          ],
        ),
      ),
    );
  }
}