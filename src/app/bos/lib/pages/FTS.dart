import 'package:flutter/material.dart';
import 'consumer/TableNumberPage.dart';

class FTSPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text("First time setup!")
        ),
        body: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              _fab(
                context,
                "receptionButton",
                "Reception",
                () {}
              ),
              _fab(
                context,
                "consumerButton",
                "Consumer",
                () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => TableNumberPage())
                  );
                }
              ),
              _fab(
                context,
                "kitchenButton",
                "Kitchen",
                () {}
              ),
            ],
          ),
        ),
      )
    );
  }
}

Widget _fab(context, herotag, label, onPressed) {
  return Container(
    height: 125,
    width: (MediaQuery.of(context).size.width) / 4,
    child: FloatingActionButton(
      heroTag: herotag,
      child: Text(label),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(16.0))),
      onPressed: onPressed,
    )
  );
}