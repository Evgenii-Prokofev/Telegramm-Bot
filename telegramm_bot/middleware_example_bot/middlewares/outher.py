import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class FirstOutherMiddleware(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        logger.debug(
            'Вошли в мидллварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        result = await handler(event, data)
        
        logger.debug('Выходим из мидллвари %s', __class__.__name__)
        
        return result


class SecondOutherMiddleware(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        logger.debug(
            'Вошли в мидллварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        result = await handler(event, data)
        
        logger.debug('Выходим из мидллвари %s', __class__.__name__)
        
        return result
            
    
class ThirdOutherMiddleware(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        logger.debug(
            'Вошли в мидллварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )
        
        result = await handler(event, data)
        
        logger.debug('Выходим из мидллвари %s', __class__.__name__)
        
        return result
