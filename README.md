# CandyFloss
Let's make candy floss with a baxter!!

## Baxterラクチンセットアップ
1. catkin_wsの下にリポジトリをクローンして`setup.sh`を実行する。
   パスワード入力求められたり、いろいろ聞かれるけど適当に対応してあげて

       $ cd catkin_ws/src
       $ clone https://github.com/p-robobu/candy_floss.git
       $ bash ./setup.sh

## baxter ノードから指定ポイントへ動かす

1. baxterのガゼボを起動

       $ roslaunch baxter_gazebo baxter_world.launch

2. baxterの腕を初期位置に移動させるノード ※ムーブイット系を実行中は動作できない
   最初に初期位置にしないと自作ノードのポイントに動作できないので必ず実行する

       $ rosrun baxter_tools tuck_arms.py -u

3. これをしないとムーブイットが動作しない

       $ rosrun baxter_interface joint_trajectory_action_server.py

4. baxterのムーブイットrvizを起動するコマンド ※これを起動しないと自作ノードが動かない

       $ roslaunch baxter_moveit_config baxter_grippers.launch

5. 自作ノードで腕を動かす

       $ rosrun candy_floss test_arm_moving 

## 指定ポイントの作り方

1. baxterのガゼボを起動

       $ roslaunch baxter_gazebo baxter_world.launch

2. キーボードでバクスターの腕を指定したいポイントへ動かす 起動したら一度エンターを押す
   ※rosrun baxter_interface joint_trajectory_action_server.py が動いているときは動作しない

       $ rosrun baxter_examples joint_position_keyboard.py

3. 現在のハンドの姿勢の座標を取得する 
   poseのpositionとorientationの値をメモしてtest_arm_moving.cppに記入する

       $ rostopic echo /robot/limb/left/endpoint_state 
       $ rostopic echo /robot/limb/right/endpoint_state 


