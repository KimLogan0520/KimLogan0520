import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Hello World!',
                style: TextStyle(
                  fontSize: 16.0,
                  fontWeight: FontWeight.w700,
                  color: Colors.blue,
                ),
              ),
              TextButton(
                onPressed: (){},
                style: TextButton.styleFrom(foregroundColor: Colors.red),
                child: Text('텍스트 버튼'),
              ),
              OutlinedButton(
                onPressed: (){},
                style: OutlinedButton.styleFrom(foregroundColor: Colors.red),
                child: Text('아웃라인드 버튼'),
              ),
              ElevatedButton(
                onPressed: (){},
                style: ElevatedButton.styleFrom(foregroundColor: Colors.red),
                child: Text('엘레베이티드 버튼'),
              )
            ],
          ),
        )
      )
    );
  }
}