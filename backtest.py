
def run_backtest(auto=False):
    import random
    signal = random.choice(['buy', 'sell', 'hold'])
    return {
        "signal": signal,
        "auto_executed": auto if signal in ['buy', 'sell'] else False,
        "details": f"Simulated {signal} action."
    }
