# cat-pi-monitor
Monitor your cat in local network by Raspberry PI Camera and upload it to cloud server.

### gRPC

```shell
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. monitor.proto
```

### Developing

* export PYTHONPATH=${PYTHONPATH}:/home/ubuntu/codes/cat-pi-monitor

## TODO list

- [ ] A web interface for 
    - [ ] 显示已保存的视频
- [ ] 一个队列可以保存一定长度的视频数据
- [ ] 有人访问的时候客户端才上传数据
    * 修改servicer的Reply，阻塞客户端的上传
- [ ] 图片转视频流，流量优化
    * 测试一下现在的带宽能否跑满30帧
    * 1Mbps带宽，512×512一秒一张
- [x] 图片加入时间戳
- [ ] 目标检测
- [ ] 消除重复帧
    * data为0代表没有变化
- [ ] 异常事件重启
    - [ ] 服务器宕机

## References

- [opencv-stream-video-to-web-browser-html-page/](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
- [install opencv on raspberry pi](https://zhuanlan.zhihu.com/p/92184435)

## Solution

* gRPC didn't work
    - The data generator/function has bugs, test it!