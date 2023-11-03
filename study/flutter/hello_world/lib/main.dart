import 'package:flutter/material.dart';

/// Default App
// void main(){
//   runApp(MyApp());
// }
//
// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: SizedBox(
//           width: double.infinity,
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: [
//               Text(
//                 'Hello World!',
//                 style: TextStyle(
//                   fontSize: 16.0,
//                   fontWeight: FontWeight.w700,
//                   color: Colors.blue,
//                 ),
//               ),
//               TextButton(
//                 onPressed: (){},
//                 style: TextButton.styleFrom(foregroundColor: Colors.red),
//                 child: Text('텍스트 버튼'),
//               ),
//               OutlinedButton(
//                 onPressed: (){},
//                 style: OutlinedButton.styleFrom(foregroundColor: Colors.red),
//                 child: Text('아웃라인드 버튼'),
//               ),
//               ElevatedButton(
//                 onPressed: (){},
//                 style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
//                 child: Text('엘레베이티드 버튼'),
//               ),
//               IconButton(
//                 onPressed: (){},
//                 icon: Icon(
//                   Icons.home, // https://fonts.google.com/icons
//                 ),
//               ),
//               GestureDetector(
//                 onTap: (){
//                   print('on tap');
//                 },
//                 onDoubleTap: (){
//                   print('on double tap');
//                 },
//                 onLongPress: (){
//                   print('on long press');
//                 },
//                 child: Container(
//                   decoration: BoxDecoration(
//                     color: Colors.orange,
//                   ),
//                   width: 100.0,
//                   height: 100.0,
//                 ),
//               )
//             ],
//           ),
//         )
//       )
//     );
//   }
// }

/// FloatingActionButtonExample
// void main() {
//   runApp(FloatingActionButtonExample());
// }

// class FloatingActionButtonExample extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         floatingActionButton: FloatingActionButton(
//           onPressed: () {},
//           child: Text('클릭'),
//         ),
//
        // body: Container(
        //   decoration: BoxDecoration(
        //     color: Colors.red,
        //     border: Border.all(
        //       width: 16.0,
        //       color: Colors.black,
        //     ),
        //     borderRadius: BorderRadius.circular(
        //       16.0,
        //     ),
        //   ),
        //   height: 200.0,
        //   width: 100.0,
        // ),

        // body: SafeArea(
        //   top: true,
        //   bottom: true,
        //   left: true,
        //   right: true,
        //   child: Container(
        //       color: Colors.black,
        //       child: Container(
        //           color: Colors.blue,
        //           margin: EdgeInsets.all(16.0),
        //           child: Padding(
        //             padding: EdgeInsets.all(16.0),
        //             child: Container(
        //               color: Colors.yellow,
        //               width: 50,
        //               height: 50,
        //             ),
        //           )
        //       )
        //   ),
        // )

      // ),
    // );
  // }
// }

/// Row Widget
// void main() {
//   runApp(RowWidgetExample());
// }
//
// class RowWidgetExample extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: SizedBox(
//           height: double.infinity, // 반대축에서 이동할 공간을 제공하기 위해 높이를 최대한으로 지정
//           child: Row(
//             mainAxisAlignment: MainAxisAlignment.spaceEvenly, // 주축 정렬 지정
//             crossAxisAlignment: CrossAxisAlignment.stretch, // 반대축 정렬 지정
//             children: [
//               Container(
//                 height: 50.0,
//                 width: 50.0,
//                 color: Colors.red,
//               ),
//
//               const SizedBox(width: 12.0,),
//
//               Container(
//                 height: 50.0,
//                 width: 50.0,
//                 color: Colors.green,
//               ),
//
//               const SizedBox(width: 12.0,),
//
//               Container(
//                 height: 50.0,
//                 width: 50.0,
//                 color: Colors.blue,
//               ),
//             ],
//           ),
//         ),
//       )
//     );
//   }
// }

/// Column Widget
// void main() {
//   runApp(ColumnWidgetExample());
// }

// class ColumnWidgetExample extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: SizedBox(
//           width: double.infinity,
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.spaceEvenly,
//             crossAxisAlignment: CrossAxisAlignment.center,
//             children: [
//               Flexible(
                // flex는 남은 공간을 차지할 비율을 의미, flex값을 제공하지 않으면 기본값은 1
                // flex: 1,
                // child: Container(
                //   color: Colors.blue,
                // ),
              // ),
              // Flexible(
              //   flex: 3,
              //   child: Container(
              //     color: Colors.red,
              //   )
              // )

              // Container(
              //   height: 50.0,
              //   width: 50.0,
              //   color: Colors.red,
              // ),
              //
              // const SizedBox(width: 12.0,),
              //
              // Container(
              //   height: 50.0,
              //   width: 50.0,
              //   color: Colors.green,
              // ),
              //
              // const SizedBox(width: 12.0,),
              //
              // Container(
              //   height: 50.0,
              //   width: 50.0,
              //   color: Colors.blue,
              // )
            // ],
          // ),
        // ),
      // )
    // );
  // }
// }

/// Expanded Widget
// void main() {
//   runApp(ExpandedWidgetExample());
// }
//
// class ExpandedWidgetExample extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//         home: Scaffold(
//           body: SizedBox(
//             width: double.infinity,
//             child: Column(
//               children: [
//                 Expanded(
//                   child: Container(
//                     color: Colors.blue,
//                   ),
//                 ),
//                 Expanded(
//                   child: Container(
//                     color: Colors.red,
//                   )
//                 )
//               ],
//             ),
//           ),
//         )
//     );
//   }
// }

/// Stack Widget
void main() {
  runApp(StackWidgetExample());
}

class StackWidgetExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
          body: SizedBox(
            width: double.infinity,
            child: Stack(
              children: [
                Container(
                  height: 300.0,
                  width: 300.0,
                  color: Colors.red,
                ),
                Container(
                  height: 250.0,
                  width: 250.0,
                  color: Colors.yellow,
                ),
                Container(
                  height: 200.0,
                  width: 200.0,
                  color: Colors.blue,
                )
              ],
            )
          ),
        )
    );
  }
}
