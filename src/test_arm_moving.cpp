// 参考URL　https://gbiggs.github.io/ros_moveit_rsj_tutorial/manipulators_and_moveit.html
#include <ros/ros.h>
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "test_arm_moving");
    ros::NodeHandle nh;

    //ROSのアシンクロナスな機能を初期化
    ros::AsyncSpinner spinner(2);
    spinner.start();
    //MoveIt!のAPIの初期化
    moveit::planning_interface::MoveGroupInterface left_arm("left_arm");
    left_arm.setPoseReferenceFrame("base_link");
    moveit::planning_interface::MoveGroupInterface right_arm("right_arm");
    right_arm.setPoseReferenceFrame("base_link");



    // 動作ポイントを指定
    ROS_INFO("Start left arm moving");
    geometry_msgs::PoseStamped l_p1;
    l_p1.header.frame_id = "base_link";
    l_p1.pose.position.x = 1.24726676635;
    l_p1.pose.position.y = 0.362492379084;
    l_p1.pose.position.z = 0.276503576508;
    l_p1.pose.orientation.x = -0.255526738994;
    l_p1.pose.orientation.y = 0.66375815024;
    l_p1.pose.orientation.z = -0.197097286858;
    l_p1.pose.orientation.w = 0.674747258729;

    //指定したポイントへ動作する
    left_arm.setPoseTarget(l_p1);
    left_arm.move();
    ROS_INFO("Succeed in move to point");


    ROS_INFO("Start right arm moving");
    geometry_msgs::PoseStamped r_p1;
    r_p1.header.frame_id = "base_link";
    r_p1.pose.position.x = 1.21469227674;
    r_p1.pose.position.y = -0.326978839646;
    r_p1.pose.position.z = 0.293692538687;
    r_p1.pose.orientation.x = 0.210022899052;
    r_p1.pose.orientation.y = 0.661583673813;
    r_p1.pose.orientation.z = 0.220879314172;
    r_p1.pose.orientation.w = 0.685134842924;

    //指定したポイントへ動作する
    right_arm.setPoseTarget(r_p1);
    right_arm.move();
    ROS_INFO("Succeed in move to point");

    ros::shutdown(); // ノードの停止
    return 0;
}
