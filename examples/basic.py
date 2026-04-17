"""
Basic usage — replace client.messages.create() with TierRouter.

Requires: pip install anthropic claude-tier-router
Requires: ANTHROPIC_API_KEY env var
"""
from anthropic import Anthropic
from tier_router import TierRouter


def main():
    router = TierRouter(Anthropic())

    # Structured task -> Haiku (cheap, fast)
    resp = router.fast(
        messages=[
            {"role": "user", "content": "Extract the ticker and sentiment as JSON: 'AAPL is looking strong today'"}
        ],
        max_tokens=200,
    )
    print("FAST:", resp.content[0].text)

    # Reasoning task -> Sonnet (quality)
    resp = router.deep(
        messages=[
            {"role": "user", "content": "Review this trading strategy and name 3 weaknesses: buy when RSI < 30, sell when RSI > 70."}
        ],
        max_tokens=500,
    )
    print("\nDEEP:", resp.content[0].text)

    # Cost receipt
    print("\n", router.cost_breakdown())


if __name__ == "__main__":
    main()
