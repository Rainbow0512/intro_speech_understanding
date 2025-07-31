import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    
    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples
    
    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames
    
    num_frames should be at least int((len(speech)-frame_length)/step); it may be longer.
    For every n and t such that 0 <= t*step+n <= N-1, it should be the case that 
       frames[n,t] = waveform[t*step+n]
    '''
    num_frames = int(np.floor((len(waveform) - frame_length) / step)) + 1
    frames = np.zeros((frame_length, num_frames))
    
    for t in range(num_frames):
        start_index = t * step
        frames[:, t] = waveform[start_index : start_index + frame_length]
        
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    
    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)
    
    @returns:
    stft (np.ndarray((frame_length,num_frames))) - the STFT (complex-valued)
    '''
    stft = np.fft.fft(frames, axis=0)
    
    return stft

def stft_to_spectrogram(stft):
    '''
    Calculate the level, in decibels, of each complex-valued sample of the STFT,
    normalized so the highest value is 0dB, 
    and clipped so that the lowest value is -60dB.
    
    @params:
    stft (np.ndarray((frame_length,num_frames))) - STFT (complex-valued)
    
    @returns:
    spectrogram (np.ndarray((frame_length,num_frames)) - spectrogram (real-valued)
    
    The spectrogram should be expressed in decibels (20*log10(abs(stft)).
    np.amax(spectrogram) should be 0dB.
    np.amin(spectrogram) should be no smaller than -60dB.
    '''
    magnitudes = np.abs(stft)
    max_magnitude = np.amax(magnitudes)
    
    if max_magnitude == 0:
        return np.full(stft.shape, -60.0)
        
    normalized_magnitudes = magnitudes / max_magnitude
    
    floored_magnitudes = np.maximum(normalized_magnitudes, 1e-6)
    spectrogram_db = 20 * np.log10(floored_magnitudes)
    clipped_spectrogram = np.maximum(spectrogram_db, -60)
    
    return clipped_spectrogram


