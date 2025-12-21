from app.mcp.context import StartupContext
from app.services.huggingface import (
    get_sentiment_pipeline,
    get_zero_shot_pipeline
)
from app.utils.logger import logger

class MarketAgent:
    name = "market_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Market Agent started")
        context.current_agent = self.name

        idea_text = context.idea

        # 1️⃣ Sentiment (proxy for market perception)
        sentiment_pipe = get_sentiment_pipeline()
        sentiment = sentiment_pipe(idea_text)[0]

        sentiment_score = (
            sentiment["score"] if sentiment["label"] == "POSITIVE"
            else 1 - sentiment["score"]
        )

        # 2️⃣ Demand classification (zero-shot)
        zero_shot = get_zero_shot_pipeline()
        demand_labels = ["high demand", "medium demand", "low demand"]

        demand_result = zero_shot(
            idea_text,
            candidate_labels=demand_labels
        )

        demand_label = demand_result["labels"][0]
        demand_confidence = demand_result["scores"][0]

        # 3️⃣ Compute final market score
        market_score = round(
            (sentiment_score * 0.4) +
            (demand_confidence * 0.6),
            3
        )

        # 4️⃣ Update context
        context.market_score = market_score
        context.completed_agents.append(self.name)

        logger.info(
            f"Market Agent completed | "
            f"sentiment={sentiment_score:.2f}, "
            f"demand={demand_label} ({demand_confidence:.2f}), "
            f"market_score={market_score}"
        )

        return context
