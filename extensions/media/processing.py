class MediaProcessor:
    def __init__(self):
        self.pipelines = {
            'image': [Enhance(), Compress(), Watermark()],
            'video': [Transcode(), Stabilize(), Analyze()]
        }
        
    async def process(self, media_file, media_type):
        pipeline = self.pipelines.get(media_type, [])
        result = media_file
        for processor in pipeline:
            result = await processor.apply(result)
        return result
    
    def add_processor(self, media_type, processor):
        self.pipelines.setdefault(media_type, []).append(processor)
