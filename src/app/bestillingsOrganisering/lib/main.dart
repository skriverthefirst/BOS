import 'package:flutter/material.dart';
import 'pages/FTS.dart';
import 'pages/consumer/TableNumberPage.dart';
import 'pages/globals/globals.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: determinePage()
    );
  }
}

Widget determinePage() {
  if(isFTS) {
    return TableNumberPage();
  } else {
    return FTSPage();
  }
}