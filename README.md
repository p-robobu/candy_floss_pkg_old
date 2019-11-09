# CandyFloss
Let's make candy floss with a baxter!!




## baxter ノードから指定ポイントへ動かす

    1. baxterのガゼボを起動
       $ roslaunch baxter_gazebo baxter_world.launch

    2. baxterの腕を初期位置に移動させるノード ※ムーブイット系を実行中は動作できない
       最初に初期位置にしないと自作ノードのポイントに動作できないので必ず実行する
       $ rosrun baxter_tools tuck_arms.py -u



    3. よくわからないコマンド これをしないとムーブイットが動作しない
       $ rosrun baxter_interface joint_trajectory_action_server.py

    4. baxterのムーブイットrvizを起動するコマンド これを起動しないと自作ノードが動かない？
       $ roslaunch baxter_moveit_config baxter_grippers.launch

    5. 自作ノードで腕を動かす
       $ rosrun candy_floss test_arm_moving 



