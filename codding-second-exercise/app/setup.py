import logging

# Preparing a simplified log
formatter = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger = logging.getLogger("machine")
logger.addHandler(console)
logger.setLevel(logging.INFO)
