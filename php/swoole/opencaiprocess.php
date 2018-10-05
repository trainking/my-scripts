<?php

class OpencaiProcess{

    public $mpid = 0; // 主进程id
    public $works = [];  // 子进程数组
    public $max_precess = 4;  // 最大的进程数
    public $new_index = 0;  // 最新下标
    public $callback = null;

    public function __construct(int $max_precess, $callback)
    {
        try {
            swoole_set_process_name(sprintf('opencai-ps：%s', 'master'));
            $this->mpid = posix_getpid();
            $this->max_precess = $max_precess;
            $this->callback = $callback;
            $this->run();
            $this->processWait();
        } catch (\Exception $e) {
            die("ERROR：".$e->getMessage());
        }
    }

    /**
     * 执行创建子进程执行
     */
    public function run() {
        for ($i = 0; $i < $this->max_precess; $i++) {
            $this->createProcess($i);
        }
    }

    /**
     * 创建子进程
     * @param null $index
     * @return int
     */
    public function createProcess($index = null) {
        $process = new swoole_process(function (swoole_process $worker) use ($index) {
            if (is_null($index)) {
                $index = $this->new_index;
                $this->new_index ++;
            }
            swoole_set_process_name(sprintf('opencai-ps: %s', $index));
//            opencai_callback();
            call_user_func($this->callback);
        }, false, false);
        $pid = $process->start();
        $this->works[$index] = $pid;
        return $pid;
    }

    /**
     * 重启子进程
     * @param $ret
     * @throws Exception
     */
    public function rebootProcess($ret){
        $pid=$ret['pid'];
        $index=array_search($pid, $this->works);
        if($index!==false){
            $index=intval($index);
            $new_pid=$this->createProcess($index);
            // TODO 记录重启日志
            return;
        }
        throw new \Exception('rebootProcess Error: no pid');
    }

    /**
     * 进程等待
     */
    public function processWait() {
        while (true) {
            if (count($this->works)) {
                $ret = swoole_process::wait();
                if ($ret) {
                    $this->rebootProcess($ret);
                }
            } else {
                break;
            }
        }
    }
}
