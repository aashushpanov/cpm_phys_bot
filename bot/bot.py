import asyncio
import logging
from loader import bot, dp
from handlers import handlers_router


logging.basicConfig(level=logging.INFO)

dp.include_routers(
    handlers_router
)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
