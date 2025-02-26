import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO
    format="%(asctime)s %(levelname)s: %(message)s",  # 日志格式
    datefmt="%H:%M:%S,%f",  # 时间戳的格式
)

# 创建一个文件处理器，将日志输出到文件
file_handler = logging.FileHandler("/tmp/park.log", mode='w')
file_handler.setLevel(logging.INFO)  # 设置文件处理器的日志级别
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s", datefmt="%H:%M:%S,%f"))

# 获取根日志记录器
logger = logging.getLogger()

# 将文件处理器添加到根日志记录器
logger.addHandler(file_handler)

# 测试日志
logger.info("This is an info message3")
logger.warning("This is a warning message3")
logger.error("This is an error message")
