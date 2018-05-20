#!/bin/bash
#############################################################
#celery flower web ui controller script
#start_celery_flower: 启动celery的ui web界面
#start_celery_app： 启动celery worker，启动服务
#params:
#    -A   task name
#    -l   log level
#    -c   concurrency num
############################################################
CELERY_UI_PORT=5555

BROKER="redis://127.0.0.1:6379/1"

ASYNC_TASKS="asyn_tasks"

CRON_TASKS="cron_tasks"

start_celery_flower() {
   nohup celery flower  --broker=$BROKER  --port=$CELERY_UI_PORT >./logs/flower.log 2>./flower.log  &
   echo "start celery ui server ok with $CELERY_UI_PORT"
}

#启动异步处理任务
start_async_tasks() {
  #celery worker  -A  $ASYNC_TASKS  -l info
  nohup celery worker   -A $ASYNC_TASKS  -l info -c 2 >./logs/asyn_tasks.log 2>./logs/asyn_tasks.log  &
  echo "start the async tasks ok!"
}

#测试异步处理任务
test_astasks(){
    python tests.py
}

#启动定时处理任务服务
start_crontab_tasks() {
   #celery worker  -A  $CRON_TASKS  -l info
   nohup celery worker   -A $CRON_TASKS  -l info -c 2 >./cron_tasks.log 2>.cron_tasks.log  &
   echo "start the crontab tasks ok!"
}

#发送beat，触发定时
celery_beat() {
   #celery beat  -A  $CRON_TASKS  -l info
   nohup celery beat   -A $CRON_TASKS  -l info -c 2 >./cron_tasks.log 2>.cron_tasks.log  &

}

stop_celery_app(){
  killall celery
}

celery_status() {
   ps -ef | grep celery
}

case $1 in
    flower) 
        start_celery_flower
        ;;
    atasks)
        start_async_tasks
        ;;
    test)
        test_astasks
        ;;
    ctasks)
        start_crontab_tasks
        ;;
    beat)
        celery_beat
        ;;
    status)
        celery_status
        ;;
    help)
        echo "./deploy_ctrl.sh flower(启动celery UI)
                 | atasks（启动异步处理任务）  | test （测试异步处理任务）
                 | ctasks (启动定时处理任务) | beat（测试触发定时器） | status (celery运行情况) "
        ;;
      *)
        echo "./deploy_ctl.sh flower(启动celery UI)
                 | atasks（启动异步处理任务）  | test （测试异步处理任务）
                 | ctasks (启动定时处理任务) | beat（测试触发定时器） | status (celery运行情况) "
        exit 2
esac

