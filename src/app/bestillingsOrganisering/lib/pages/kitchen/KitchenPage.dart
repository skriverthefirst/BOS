import 'package:flutter/material.dart';
import '../globals/globals.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class KitchenPage extends StatefulWidget {

  @override
  _KitchenPageState createState() => _KitchenPageState();
}

class _KitchenPageState extends State<KitchenPage> {
  Timer timer;
  String incomingJsonText = "";

  @override
  void initState() {
    super.initState();
    timer = Timer.periodic(Duration(milliseconds: 500), (Timer t) => checkForNewOrder());
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  void checkForNewOrder() async {
    http.get(getNotification).then((response){
      print(response.statusCode);
      if(response.statusCode == 200){
        var decodedResponse = utf8.decode(response.bodyBytes);
        setState(() {
          incomingJsonText = "NEW ORDER ARRIVED"; //decodedResponse
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
        ),
        body: Column(
          children: <Widget>[
            Text(incomingJsonText)
          ],
        ),
      ),
    );
  }
}