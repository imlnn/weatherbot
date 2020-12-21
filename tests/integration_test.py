import asyncio
from pyrogram import Client
from tgintegration import BotController
from tgintegration import Response

client = Client(
    "my_account",
    api_id=2409726,
    config_file="../config.ini"
)


async def run_pyrogram_client():
    controller = BotController(
        peer="@GetFastWeatherBot",
        client=client,
        max_wait=5,
        wait_consecutive=3,
        raise_no_response=True,
        global_action_delay=2.5
    )

    try:
        # 0 step: Check info
        async with controller.collect(count=1) as response:  # type: Response
            await controller.send_command("/info", None, None, False)

        assert response.num_messages == 1
        assert "You can check the weather in any location with this bot!" in response.full_text
        print(response.full_text)

        # 1 step: Check greeting
        async with controller.collect(count=2) as response:  # type: Response
            await controller.send_command("/start", None, None, False)

        assert response.num_messages == 2
        assert "Hello, " in response.full_text
        assert "Pick your option on the keyboard" in response.full_text
        print(response.full_text)

        # 2 step: Check weather now
        async with controller.collect(count=1) as response:  # type: Response
            await controller.send_command("Now", None, None, False)

        assert response.num_messages == 1
        assert "Send your City name, choose City from defaults or tap Back to return to main menu" in response.full_text
        print(response.full_text)

        # 3 step: Choose city
        async with controller.collect(count=1) as response:  # type: Response
            await controller.send_command("Moscow", None, None, False)

        assert response.num_messages == 1
        assert "Moscow" in response.full_text
        assert "Temperature" in response.full_text
        print(response.full_text)

        # 4 step: Go back and check weather in Nizhnevartovsk tomorrow
        await controller.send_command("Back", None, None, False)
        await controller.send_command("Tomorrow", None, None, False)
        async with controller.collect(count=1) as response:  # type: Response
            await controller.send_command("Nizhnevartovsk", None, None, False)

        assert response.num_messages == 1
        assert "Nizhnevartovsk" in response.full_text
        assert "Temperature" in response.full_text
        print(response.full_text)

        # 5 step: Go back and check weather in Saint Petersburg next week
        await controller.send_command("Back", None, None, False)
        await controller.send_command("Weekly", None, None, False)
        async with controller.collect(count=8) as response:  # type: Response
            await controller.send_command("Saint Petersburg", None, None, False)

        assert response.num_messages == 8
        assert "Saint Petersburg" in response.full_text
        assert "Temperature" in response.full_text
        print(response.full_text)

    finally:
        await controller.clear_chat()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run_pyrogram_client())
