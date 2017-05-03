def initialize(context):
        context.aapl = sid(24)

def handle_data(context, data):
        hist = data.history(context.aapl. 'price', 50, '1d')
        log.info(hist.head())
        sma_50 = hist.mean()
        sma_20 = hist[-20:].mean()
